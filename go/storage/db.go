package storage

import (
	"gorm.io/gorm"
	"gorm.io/driver/sqlite"
  )

var DB *gorm.DB

func NewDB(params ...string) *gorm.DB {
	DB, err := gorm.Open(sqlite.Open("test.db"), &gorm.Config{})
	if err != nil {
		panic("failed to connect database")
	}

	return DB
}

func GetDBInstance() *gorm.DB {
	return DB
}