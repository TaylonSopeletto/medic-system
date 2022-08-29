package controllers

import (
	"net/http"
	"github.com/labstack/echo/v4"
	"github.com/TaylonSopeletto/medic-system/go/models"
	"github.com/TaylonSopeletto/medic-system/go/storage"
)

func GetPatients(c echo.Context) error {
	patients, _ := GetRepoPatients()
	return c.JSON(http.StatusOK, patients)
}

func GetRepoPatients() ([]models.Patients, error) {
	db := storage.GetDBInstance()
	patients := []models.Patients{}

	if err := db.Find(&patients).Error; err != nil {
		return nil, err
	}

	return patients, nil
}