Feature: Order on swiggy

Scenario: Open browser
Given Open browser "chrome" and move to swiggy website
   When Enter location as "Indiranagar, Bengaluru" and choose correct address
       And Search restaurent "Bite Me"
       And Order item "Red Velvet Cupcake" with quantity "2"
       And Order item "Tiramisu  Cupcake" with quantity "1"
       And Order item "Irish Coffee Cupcake" with quantity "1"
       And Order item "Choco Choco Cupcake" with quantity "1"
       And Checkout and fetch all items present there
       And Verify item "Red Velvet Cupcake" is present with count "2" on checkout page
       And Verify item "Tiramisu Cupcake" is present with count "1" on checkout page
       And Enter details as mobileno "0000000000" and name "abc abc" and email "abc@def.com" and password "abcdef" while signup
       Then Verify email error and take screenshot
       And On checkout page update item "Red Velvet Cupcake" with quantity as "1"
       And I take a screenshot
