package com.lcwd.Hotel.exceptions;

public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String idNotFound) {
        super(idNotFound);
    }

    public ResourceNotFoundException()
    {
        super("Resource not found");
    }
}
