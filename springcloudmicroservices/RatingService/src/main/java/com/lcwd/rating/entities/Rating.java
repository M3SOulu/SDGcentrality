package com.lcwd.rating.entities;

import lombok.*;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder

@Document("user_ratings")
public class Rating {

    @Id
    private  String ratingId;
    private  String userId;
    private String hotelId;
    private int rating;
    private String feedback;

}
