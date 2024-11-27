package com.lcwd.Hotel.services;

import com.lcwd.Hotel.entities.Hotel;

import java.util.List;

public interface HotelService {

    Hotel save(Hotel hotel);

    Hotel getById(String id);

    List<Hotel> getALL();

}
