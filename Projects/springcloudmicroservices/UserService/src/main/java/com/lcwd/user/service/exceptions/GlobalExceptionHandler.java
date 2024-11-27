package com.lcwd.user.service.exceptions;

import com.lcwd.user.service.payload.ApiResponse;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;

@RestControllerAdvice
public class GlobalExceptionHandler {

    @ExceptionHandler(ResourceNotFoundException.class)
    public ResponseEntity<ApiResponse> handlerResourceNotFoundException(ResourceNotFoundException ex)
    {
        String Message = ex.getMessage();
        ApiResponse response = ApiResponse.builder().message(Message).status(HttpStatus.NOT_FOUND).success(true).build();
        return  new ResponseEntity<ApiResponse>(response,HttpStatus.NOT_FOUND);
    }
}
