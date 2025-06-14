package middleware

import (
	"log/slog"
	"net/http"
)

type middleware struct {
	logger *slog.Logger
}

func New(logger *slog.Logger) *middleware {
	return &middleware{
		logger: logger,
	}
}

func (m *middleware) HTTPMiddleware(next http.Handler) http.Handler {
	return http.HandlerFunc(func(w http.ResponseWriter, r *http.Request) {
		defer func() {
			if err := recover(); err != nil {
				m.logger.ErrorContext(r.Context(), "Recovered from panic", "error", err)
				http.Error(w, "Internal Server Error", http.StatusInternalServerError)
			}
		}()
		next.ServeHTTP(w, r)
	})
}