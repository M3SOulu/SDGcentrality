package com.lcwd.Hotel.repositories;

import com.lcwd.Hotel.entities.Hotel;
import org.springframework.data.jpa.repository.JpaRepository;

public interface HotelRepository extends JpaRepository<Hotel,String>
{
}
