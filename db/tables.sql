CREATE TABLE IF NOT EXISTS t_users (user_id integer PRIMARY KEY, user_name_first text NOT NULL, user_name_last text NOT NULL, user_phone text NOT NULL, user_dni text NOT NULL);
CREATE TABLE IF NOT EXISTS t_users_locations (location_id integer PRIMARY KEY, user_id integer NOT NULL, location_address text NOT NULL, location_city text NOT NULL, location_country text NOT NULL, location_zip text NOT NULL, FOREIGN KEY (user_id) REFERENCES t_users (user_id) ON DELETE CASCADE ON UPDATE CASCADE);
CREATE TABLE IF NOT EXISTS t_users_records (record_id integer PRIMARY KEY, user_id integer NOT NULL, record_title text NOT NULL, record_year text NOT NULL, FOREIGN KEY (user_id) REFERENCES t_users (user_id) ON DELETE CASCADE ON UPDATE CASCADE);