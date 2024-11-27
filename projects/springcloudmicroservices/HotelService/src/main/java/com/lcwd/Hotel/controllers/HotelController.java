package com.lcwd.Hotel.controllers;

import com.lcwd.Hotel.entities.Hotel;
import com.lcwd.Hotel.services.HotelService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.servlet.function.EntityResponse;

import java.util.List;

@RestController
@RequestMapping("/hotels")
public class HotelController
{

    @Autowired
    private HotelService hotelService;
    //Create

    @PostMapping
    public ResponseEntity<Hotel> createHotel(@RequestBody Hotel hotel)
    {
        return ResponseEntity.status(HttpStatus.CREATED)
                .body(hotelService.save(hotel));
    }

    @GetMapping("/{hotelId}")
    public ResponseEntity<Hotel> GetById(@PathVariable  String hotelId)
    {
        return ResponseEntity.ok(hotelService.getById(hotelId));
    }

    @GetMapping
    public ResponseEntity<List<Hotel>> GetALL()
    {
        return ResponseEntity.ok(hotelService.getALL());
    }

}
