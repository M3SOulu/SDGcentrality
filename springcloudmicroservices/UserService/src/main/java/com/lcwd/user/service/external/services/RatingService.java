package com.lcwd.user.service.external.services;

import com.lcwd.user.service.entities.Rating;
import org.springframework.cloud.openfeign.FeignClient;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.PutMapping;

@FeignClient(name = "RATING-SERVICE")
@Service
public interface RatingService {

    @GetMapping("/ratings/users/{userId}")
    Rating getRatings(@PathVariable("userId") String userId);

    @PostMapping("/ratings")
    public Rating   createRating(Rating values);

    @PutMapping("/ratings/{ratingId}")
    public  Rating updateRating(@PathVariable("ratingId") String ratingId, Rating rating);
}
