package com.microservice.hospitalmanageservice.service;

import com.microservice.hospitalmanageservice.entity.dto.AppointmentDto;

import java.util.Map;

public interface IAppointmentService {
    Map<Object, Long> getByDoctorIdAndDay(String hospitalId, String doctorId, String day);

    void add(String hospitalId, AppointmentDto appointmentDto);

    void removeById(String hospitalId, String id);
    void modify(String hospitalId, AppointmentDto appointmentDto);
}
