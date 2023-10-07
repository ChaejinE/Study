CREATE TYPE user_status AS ENUM ('active', 'deleted', 'blocked');
CREATE TYPE sns_type AS ENUM ('FB', 'G', 'K');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    user_status user_status DEFAULT 'active',
    email VARCHAR(255),
    pw VARCHAR(2000),
    name VARCHAR(255),
    phone_number VARCHAR(20) UNIQUE,
    profile_img VARCHAR(1000),
    sns_type sns_type,
    marketing_agree BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);