-- 5. Email validation to sent
-- resets the attribute valid_email only when the email has been changed
CREATE TRIGGER reset_validation BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
    IF NEW.email <> OLD.email THEN
    SET NEW.valid_email = 0;
    END IF;
END;
