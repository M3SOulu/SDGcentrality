package com.microservice.hospitalmanageservice.service.Impl;

import cn.hutool.core.bean.BeanUtil;
import cn.hutool.core.bean.copier.CopyOptions;
import com.microservice.common.api.CommonResult;
import com.microservice.hospitalmanageservice.client.PersonInfoClient;
import com.microservice.hospitalmanageservice.entity.dto.*;
import com.microservice.hospitalmanageservice.entity.vo.AppointmentVo;
import com.microservice.hospitalmanageservice.service.IAppointmentService;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.env.Environment;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import java.text.MessageFormat;
import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.*;
import java.util.stream.Collectors;

@Slf4j

@Service
public class AppointmentServiceImpl implements IAppointmentService {
    private final Environment environment;
    private final RestTemplate restTemplate;
    private final PersonInfoClient personInfoClient;

    private final String[] targetHours = {"08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00"};

    @Autowired
    public AppointmentServiceImpl(Environment environment, RestTemplate restTemplate, PersonInfoClient personInfoClient) {
        this.environment = environment;
        this.restTemplate = restTemplate;
        this.personInfoClient = personInfoClient;
    }

    @Override
    public Map<Object, Long> getByDoctorIdAndDay(String hospitalId, String doctorId, String day) {
        String url = MessageFormat.format(Objects.requireNonNull(environment.getProperty("api.his" + hospitalId + ".appointment.byDoctorIdAndDay")), doctorId, day);
        log.info(url);
        ResponseEntity<HashMap> responseEntity = restTemplate.getForEntity(url, HashMap.class);
        List<?> sourceList = (List<?>) Objects.requireNonNull(responseEntity.getBody()).get("data");
        List<AppointmentVo> appointmentVos = new ArrayList<>();
        switch (hospitalId) {
            case "1":
                List<AppointmentDto1> appointments1 = sourceList.stream()
                        .map(element -> BeanUtil.copyProperties(element, AppointmentDto1.class))
                        .collect(Collectors.toList());
                for (AppointmentDto1 appointmentDto1 : appointments1) {
                    AppointmentVo appointmentVo = new AppointmentVo();
                    BeanUtil.copyProperties(appointmentDto1,appointmentVo);
                    appointmentVo.setAppointmentId(appointmentDto1.getId().toString());
                    appointmentVo.setAppointmentDateTime(appointmentDto1.getTreatmentTime());
                    appointmentVo.setDeptId(11);
                    appointmentVo.setPatientCondition(appointmentDto1.getConditionDescription());
                    log.info(appointmentVo.toString());
                    appointmentVos.add(appointmentVo);
                }
                break;
            case "2":
                List<AppointmentDto2> appointments2 = sourceList.stream()
                        .map(element -> BeanUtil.copyProperties(element, AppointmentDto2.class))
                        .collect(Collectors.toList());
                for (AppointmentDto2 appointmentDto2 : appointments2) {
                    AppointmentVo appointmentVo = new AppointmentVo();
                    BeanUtil.copyProperties(appointmentDto2,appointmentVo);
                    appointmentVos.add(appointmentVo);
                }
                break;
            case "3":
                List<AppointmentDto3> appointments3 = sourceList.stream()
                        .map(element -> BeanUtil.copyProperties(element, AppointmentDto3.class))
                        .collect(Collectors.toList());
                for (AppointmentDto3 appointmentDto3 : appointments3) {
                    AppointmentVo appointmentVo = new AppointmentVo();
                    BeanUtil.copyProperties(appointmentDto3,appointmentVo);
                    appointmentVos.add(appointmentVo);
                }
                break;
        }
        log.info(appointmentVos.toString());
        // 查询每个时间段的人数
        Map<Object, Long> appointmentCountByHour = appointmentVos.stream()
                .collect(Collectors.groupingBy(
                        appointmentVo1 -> getHourRange(appointmentVo1.getAppointmentDateTime()),
                        TreeMap::new,
                        Collectors.counting()
                ));

        for (Map.Entry<Object, Long> entry : appointmentCountByHour.entrySet()) {
            log.info(entry.getKey().toString()+"="+entry.getValue().toString());
            entry.setValue((long) (entry.getValue() > 6 ? 0 : 1));
        }

        for (String hour : targetHours) {
            if (!appointmentCountByHour.containsKey(LocalTime.parse(hour))) {
                appointmentCountByHour.put(LocalTime.parse(hour), 1L);
            }
        }

        return appointmentCountByHour;
    }

    @Override
    public void add(String hospitalId, AppointmentDto appointmentDto) {
        //TODO：根据病人的id调用病人的详细信息
        CommonResult patient = personInfoClient.getPatientById(appointmentDto.getUserName());
        CommonResult doctor = personInfoClient.getDoctorById(Integer.valueOf(appointmentDto.getDoctorId()));
        PatientDto patientDto = BeanUtil.copyProperties(patient.getData(), PatientDto.class);
        DoctorDto doctorDto = BeanUtil.copyProperties(doctor.getData(), DoctorDto.class);
        log.info(doctor.toString());
        //创建post对象并赋值
        Object newAppointmentDto = new Object();
        // 调用第三方api
        String url = Objects.requireNonNull(environment.getProperty("api.his" + hospitalId + ".appointment.add"));
        switch (hospitalId) {
            case "1":
                AppointmentDto1 appointmentDto1 = new AppointmentDto1();
                appointmentDto1.setDoctorId(doctorDto.getJobNumber());
                appointmentDto1.setPatientId(patientDto.getIdNumber());
                appointmentDto1.setDept("口腔科");
                appointmentDto1.setPatientName(patientDto.getName());
                appointmentDto1.setPatientGender(patientDto.getGender().equals("男") ? 1 : 2);
                appointmentDto1.setPatientAge(LocalDate.now().getYear() - LocalDate.parse(patientDto.getBirthday()).getYear());
                appointmentDto1.setTreatmentTime(appointmentDto.getAppointmentDateTime());
                appointmentDto1.setConditionDescription(appointmentDto.getPatientCondition());
                log.info(appointmentDto1.toString());
                newAppointmentDto = appointmentDto1;
                break;
            case "2":
                AppointmentDto2 appointmentDto2 = new AppointmentDto2();
                appointmentDto2.setPatientId(patientDto.getIdNumber());
                appointmentDto2.setDoctorId(doctorDto.getJobNumber().toString());
                appointmentDto2.setDeptId(11);
                appointmentDto2.setPatientName(patientDto.getName());
                appointmentDto2.setPatientGender(patientDto.getGender().equals("男") ? 1 : 0);
                appointmentDto2.setPatientBirth(patientDto.getBirthday());
                appointmentDto2.setAppointmentDateTime(appointmentDto.getAppointmentDateTime());
                appointmentDto2.setPatientCondition(appointmentDto.getPatientCondition());
                log.info(appointmentDto2.toString());
                newAppointmentDto = appointmentDto2;
                break;
            case "3":
                AppointmentDto3 appointmentDto3 = new AppointmentDto3();
                appointmentDto3.setPatientId(patientDto.getIdNumber());
                appointmentDto3.setDoctorId(doctorDto.getJobNumber().toString());
                appointmentDto3.setDeptId(11);
                appointmentDto3.setPatientName(patientDto.getName());
                appointmentDto3.setPatientGender(patientDto.getGender().equals("男") ? 1 : 0);
                appointmentDto3.setPatientBirth(patientDto.getBirthday());
                appointmentDto3.setAppointmentDateTime(appointmentDto.getAppointmentDateTime());
                appointmentDto3.setPatientCondition(appointmentDto.getPatientCondition());
                log.info(appointmentDto3.toString());
                newAppointmentDto = appointmentDto3;
                break;
        }
        // 设置请求头
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        // 设置请求体数据
        HttpEntity<Object> request = new HttpEntity<>(newAppointmentDto, headers);
        // 发送POST请求
        ResponseEntity<String> response = restTemplate.postForEntity(url, request, String.class);
    }

    @Override
    public void removeById(String hospitalId, String id) {
        String url = MessageFormat.format(Objects.requireNonNull(environment.getProperty("api.his" + hospitalId + ".appointment.deleteById")), id);
        restTemplate.delete(url);
    }

    @Override
    public void modify(String hospitalId, AppointmentDto appointmentDto) {
        CommonResult patient = personInfoClient.getPatientById(appointmentDto.getUserName());
        CommonResult doctor = personInfoClient.getDoctorById(Integer.valueOf(appointmentDto.getDoctorId()));
        PatientDto patientDto = BeanUtil.copyProperties(patient.getData(), PatientDto.class);
        DoctorDto doctorDto = BeanUtil.copyProperties(doctor.getData(), DoctorDto.class);
        //创建post对象并赋值
        Object newAppointmentDto = new Object();
        // 调用第三方api
        String url = Objects.requireNonNull(environment.getProperty("api.his" + hospitalId + ".appointment.add"));
        switch (hospitalId) {
            case "1":
                AppointmentDto1 appointmentDto1 = new AppointmentDto1();
                appointmentDto1.setDoctorId(doctorDto.getJobNumber());
                appointmentDto1.setPatientId(patientDto.getIdNumber());
                appointmentDto1.setTreatmentTime(appointmentDto.getAppointmentDateTime());
                newAppointmentDto = appointmentDto1;
                break;
            case "2":
                AppointmentDto2 appointmentDto2 = new AppointmentDto2();
                appointmentDto2.setPatientId(patientDto.getIdNumber());
                appointmentDto2.setDoctorId(doctorDto.getJobNumber().toString());
                appointmentDto2.setAppointmentDateTime(appointmentDto.getAppointmentDateTime());
                newAppointmentDto = appointmentDto2;
                break;
            case "3":
                AppointmentDto3 appointmentDto3 = new AppointmentDto3();
                appointmentDto3.setPatientId(patientDto.getIdNumber());
                appointmentDto3.setDoctorId(doctorDto.getJobNumber().toString());
                appointmentDto3.setAppointmentDateTime(appointmentDto.getAppointmentDateTime());
                newAppointmentDto = appointmentDto3;
                break;
        }
        log.info(newAppointmentDto.toString());
        // 设置请求头
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);
        // 设置请求体数据
        HttpEntity<Object> request = new HttpEntity<>(newAppointmentDto, headers);
        // 发送POST请求
        restTemplate.put(url, request);
    }

    private static LocalTime getHourRange(LocalDateTime localDateTime) {
        int hour = localDateTime.getHour();
        return LocalTime.of(hour, 0);
    }
}