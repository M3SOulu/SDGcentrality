package com.lcwd.Hotel.impl;

import com.lcwd.Hotel.entities.Hotel;
import com.lcwd.Hotel.exceptions.ResourceNotFoundException;
import com.lcwd.Hotel.repositories.HotelRepository;
import com.lcwd.Hotel.services.HotelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.UUID;

@Service
public class HotelServiceImpl implements HotelService {

    @Autowired
    HotelRepository hotelRepository;
    @Override
    public Hotel save(Hotel hotel) {
        String Id = UUID.randomUUID().toString();
        hotel.setId(Id);
        return hotelRepository.save(hotel);
    }

    @Override
    public Hotel getById(String id) {
        return hotelRepository.findById(id).orElseThrow(() -> new ResourceNotFoundException("ID not found"));
    }

    @Override
    public List<Hotel> getALL() {
        return hotelRepository.findAll();
    }
}
