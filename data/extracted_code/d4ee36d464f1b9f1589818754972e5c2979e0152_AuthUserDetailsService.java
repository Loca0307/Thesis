package com.umg.ticket_app_backend.services;

import com.umg.ticket_app_backend.dtos.auth.AuthRegister;
import com.umg.ticket_app_backend.entities.User;
import com.umg.ticket_app_backend.repositories.UserRepository;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import com.umg.ticket_app_backend.dtos.auth.AuthRequest;
import com.umg.ticket_app_backend.dtos.auth.AuthResponse;

@Service
public class AuthService {
    private final AuthenticationManager authenticationManager;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final UserRepository userRepository;

    public AuthService(
            AuthenticationManager authenticationManager,
            PasswordEncoder passwordEncoder,
            JwtService jwtService,
            UserRepository userRepository
    ) {
        this.authenticationManager = authenticationManager;
        this.passwordEncoder = passwordEncoder;
        this.jwtService = jwtService;
        this.userRepository = userRepository;
    }

    public AuthResponse authenticate(AuthRequest authRequest) {
        final var token = new UsernamePasswordAuthenticationToken(authRequest.username(), authRequest.password());
        final var authentication = authenticationManager.authenticate(token);
        final var jwtToken = jwtService.generateToken(authentication);
        final var expiresAt = jwtService.extractExpirationTime(jwtToken);
        return new AuthResponse(jwtToken, authentication.getName(), expiresAt);
    }

    public Boolean register(AuthRegister authRequest) {
        try {
            final var newUser = new User();
            newUser.setUsername(authRequest.username());
            newUser.setPassword(passwordEncoder.encode(authRequest.password()));
            newUser.setFirstName(authRequest.firstName());
            newUser.setLastName(authRequest.lastName());

            userRepository.save(newUser);

            return true; // Registration successful
        } catch (Exception e) {
            logger.error("Error occurred during user registration: {}", e.getMessage(), e);
            return false; // Registration failed
        }
    }
}