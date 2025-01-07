
CREATE FUNCTION dbo.fn_GetLetterHash (@input NVARCHAR(100))
RETURNS NVARCHAR(100)
AS
BEGIN
    DECLARE @sorted NVARCHAR(100);

    SELECT @sorted = STRING_AGG(ch, '') WITHIN GROUP (ORDER BY ch)
    FROM (SELECT SUBSTRING(@input, value, 1) AS ch
          FROM STRING_SPLIT(REPLICATE(' ', LEN(@input)), '')
          WHERE LEN(ch) > 0) AS chars;

    RETURN @sorted;
END;
GO
