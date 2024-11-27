package com.lcwd.user.service;

import com.lcwd.user.service.entities.Rating;
import com.lcwd.user.service.external.services.RatingService;
import org.junit.jupiter.api.Test;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class UserServiceApplicationTests {

	@Test
	void contextLoads() {
	}

	@Autowired
	private RatingService ratingService;

	@Test
	void createRating()
	{
		Rating rating = Rating.builder().rating(2).userId("f7aa292a-4d27-40c6-8f7f-4498c385c547").hotelId("7b2feba4-484a-46ce-8c86-3d79baff4532").feedback("low quality feignclient").build();
		Rating savedRating = ratingService.createRating(rating);
		System.out.println("new rating created");
	}

}
