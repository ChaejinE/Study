CREATE TYPE user_status AS ENUM ('active', 'deleted', 'blocked');
CREATE TYPE sns_platform AS ENUM ('FB', 'G', 'K');

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    status user_status DEFAULT 'active',
    email VARCHAR(255),
    pw VARCHAR(2000),
    name VARCHAR(255),
    phone_number VARCHAR(20) UNIQUE,
    profile_img VARCHAR(1000),
    sns_type sns_platform,
    marketing_agree BOOLEAN DEFAULT TRUE
);