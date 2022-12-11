CREATE TABLE userinfo (
    user_number SERIAL NOT NULL,
    user_id text UNIQUE NOT NULL,
    handleName text DEFAULT 'GUEST',
    password text NOT NULL,
    PRIMARY KEY (user_number)
);
CREATE TABLE ranking (
    response_id SERIAL NOT NULL,
    user_number int DEFAULT 99999999,
    isCorrect boolean NOT NULL,
    PRIMARY KEY (response_id),
    FOREIGN KEY (user_number) REFERENCES userinfo (user_number)
);
insert into userinfo(user_number, user_id, password)
values(
        1,
        'admin',
        'c7ad44cbad762a5da0a452f9e854fdc1e0e7a52a38015f23f3eab1d80b931dd472634dfac71cd34ebc35d16ab7fb8a90c81f975113d6c7538dc69dd8de9077ec'
    );
insert into ranking(user_number, isCorrect)
values(1, true);
insert into ranking(user_number, isCorrect)
values(1, false);
insert into ranking(user_number, isCorrect)
values(1, true);
insert into ranking(user_number, isCorrect)
values(1, false);