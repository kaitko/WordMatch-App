
CREATE PROCEDURE dbo.sp_FindMatchingWords
    @letters NVARCHAR(100)
AS
BEGIN
    SET NOCOUNT ON;

    DECLARE @letterHash NVARCHAR(100) = dbo.fn_GetLetterHash(@letters);

    SELECT Word
    FROM dbo.Words
    WHERE LetterHash = @letterHash
    ORDER BY Word;
END;
GO
