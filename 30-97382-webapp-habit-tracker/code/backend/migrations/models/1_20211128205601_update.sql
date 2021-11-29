-- upgrade --
ALTER TABLE `mentalhealth` MODIFY COLUMN `rating` VARCHAR(225) NOT NULL;
-- downgrade --
ALTER TABLE `mentalhealth` MODIFY COLUMN `rating` INT NOT NULL;
