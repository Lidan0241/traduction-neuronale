#!/bin/bash

FILE_PATH="src/predictions/combined_pred_500.fr"

# Remove subword tokens
$SED_CMD "s/@@ //g" "$FILE_PATH"

#  Replace HTML entity &apos; with a single quote
$SED_CMD "s/&apos;/'/g" "$FILE_PATH"
$SED_CMD "s/' /'/g" "$FILE_PATH"

# Remove any extra spaces introduced (optional)
$SED_CMD "s/  */ /g" "$FILE_PATH"


# Ensure there is a space before certain punctuation marks
$SED_CMD "s/ *\([?!;:]\)/ \1/g" "$FILE_PATH"

# Ensure there is no space before period, comma, and final punctuation
$SED_CMD "s/ *\([.,!?]\)/\1/g" "$FILE_PATH"

# Remove leading and trailing spaces (optional)
$SED_CMD 's/^ *//g' "$FILE_PATH"
$SED_CMD 's/ *$//g' "$FILE_PATH"
