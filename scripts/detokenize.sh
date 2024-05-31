#!/bin/bash

# Detect if GNU sed or BSD sed is being used
if sed --version >/dev/null 2>&1; then
    # GNU sed (Linux)
    SED_CMD="sed -i"
else
    # BSD sed (macOS)
    SED_CMD="sed -i ''"
fi

# File path
FILE_PATH="src/predictions/Europarl_pred_500.fr"

# Step 1: Remove subword tokens
$SED_CMD "s/@@ //g" "$FILE_PATH"

# Step 2: Replace HTML entity &apos; with a single quote
$SED_CMD "s/&apos;/'/g" "$FILE_PATH"
$SED_CMD "s/' /'/g" "$FILE_PATH"

# Step 3: Remove any extra spaces introduced (optional)
$SED_CMD "s/  */ /g" "$FILE_PATH"

# Step 4: Handle punctuation (example for French)
# Ensure there is a space before certain punctuation marks
$SED_CMD "s/ *\([?!;:]\)/ \1/g" "$FILE_PATH"

# Ensure there is no space before period, comma, and final punctuation
$SED_CMD "s/ *\([.,!?]\)/\1/g" "$FILE_PATH"

# Remove leading and trailing spaces (optional)
$SED_CMD 's/^ *//g' "$FILE_PATH"
$SED_CMD 's/ *$//g' "$FILE_PATH"
