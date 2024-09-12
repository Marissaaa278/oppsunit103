#!/bin/bash
# Given three integers (, , and ) representing the three sides of a triangle, identify whether the triangle is scalene, isosceles, or equilateral.
# If all three sides are equal, output EQUILATERAL.
# Otherwise, if any two sides are equal, output ISOSCELES.
# Otherwise, output SCALENE.
# Input Format
# Three integers, each on a new line.
# Constraints
# The sum of any two sides will be greater than the third.
# Output Format
# One word: either "SCALENE" or "EQUILATERAL" or "ISOSCELES" (quotation marks excluded).
# Hint &&(and) ||(or)

# Read the sides of the triangle
read -p "side one: " side1
read -p "side two: " side2
read -p "side three: " side3

# Check if all sides are equal for equilateral triangle
if [[ $side1 -eq $side2 && $side2 -eq $side3 ]]; then
    echo "equilateral"
# Check if any two sides are equal for isosceles triangle
elif [[ $side1 -eq $side2 || $side2 -eq $side3 || $side1 -eq $side3 ]]; then
    echo "isosceles"
# Otherwise, it's a scalene triangle
else
    echo "scalene"
fi





