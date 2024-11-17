package com.lcwd.user.service.controller;

import com.lcwd.user.service.entities.User;
import com.lcwd.user.service.services.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/users")
public class UserController {

    @Autowired
    private UserService userService;
    @PostMapping
    public ResponseEntity<User> CreateUser(@RequestBody User user)
    {
        User user1 = userService.saveUser(user);
        return ResponseEntity.status(HttpStatus.CREATED).body(user1);
    }

    @GetMapping("/{userId}")
    public ResponseEntity<User> GetUserById(@PathVariable String userId)
    {
        User user1 = userService.getUserById(userId);
        return ResponseEntity.status(HttpStatus.FOUND).body(user1);
    }

    @GetMapping
    public ResponseEntity<List<User>> getAllUser()
    {
        List<User> userList = userService.getAllUsers();
        return ResponseEntity.ok(userList);
    }
}
