package com.lcwd.rating.services;

import com.lcwd.rating.entities.Rating;
import org.springframework.stereotype.Service;

import java.util.List;


public interface RatingService
{
    Rating create(Rating rating);

    List<Rating> getAllRatings();

    List<Rating> getRatingsbyUserId(String userId);

    List<Rating> getRatingsbyHotelId(String HotelId);

}
