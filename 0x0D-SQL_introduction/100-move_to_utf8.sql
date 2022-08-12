-- A script that changes the collate of a database
-- This is the command
ALTER DATABASE hbtn_0c_0 CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

ALTER TABLE hbtn_0c_0.first_table CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- ALTER TABLE first_table ALTER COLUMN name MODIFY DEFAULT CHARACTER SET utf8mb4 OLLATE utf8mb4_unicode_ci;
