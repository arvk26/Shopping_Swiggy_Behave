####Behave INSTALLATION:
- **1. install python 3.6
- **2. install pycharm tool which will create project and create virtual environment
- **3. python -m pip install behave
- **4. python -m pip install behaving
- **5. put chromedriver.exe in folder c:\Python27 folder - This folder is in path variable so no need to mention this while browser initialization

####How to execute:
 - ** Open cmd.exe and execute C:\PycharmProjects\Swiggy\venv\Scripts>activate.bat
 - ** Now move to project root folder folder C:\PycharmProjects\Swiggy\ and execute command behave. it will start test.

 Latest execution looks like below:
 ======================================
 (venv) C:\PycharmProjects\Swiggy>behave
Feature: Order on swiggy # features/order_on_swiggy.feature:1

  Scenario: Open browser                                                                                                     # features/order_on_swiggy.feature:3
    Given Open browser "chrome" and move to swiggy website                                                                   # features/steps/swiggy_steps.py:10

    When Enter location as "Indiranagar, Bengaluru" and choose correct address                                               # features/steps/swiggy_steps.py:20
	
    And Search restaurent "Bite Me"                                                                                          # features/steps/swiggy_steps.py:34
    
	And Order item "Red Velvet Cupcake" with quantity "2"                                                                    # features/steps/swiggy_steps.py:51
    
	And Order item "Tiramisu  Cupcake" with quantity "1"                                                                     # features/steps/swiggy_steps.py:51
    
	And Order item "Irish Coffee Cupcake" with quantity "1"                                                                  # features/steps/swiggy_steps.py:51
    
	And Order item "Choco Choco Cupcake" with quantity "1"                                                                   # features/steps/swiggy_steps.py:51
    
	And Checkout and fetch all items present there                                                                           # features/steps/swiggy_steps.py:71
    
	And Verify item "Red Velvet Cupcake" is present with count "2" on checkout page                                          # features/steps/swiggy_steps.py:97
    
	And Verify item "Tiramisu Cupcake" is present with count "1" on checkout page                                            # features/steps/swiggy_steps.py:97
    
	And Enter details as mobileno "0000000000" and name "abc abc" and email "abc@def.com" and password "abcdef" while signup # features/steps/swiggy_steps.py:106
    
	Then Verify email error and take screenshot                                                                              # features/steps/swiggy_steps.py:132
    
	And On checkout page update item "Red Velvet Cupcake" with quantity as "1"                                               # features/steps/swiggy_steps.py:141
    
	And I take a screenshot                                                                                                  # features/steps/swiggy_steps.py:159

1 feature passed, 0 failed, 0 skipped

1 scenario passed, 0 failed, 0 skipped

14 steps passed, 0 failed, 0 skipped, 0 undefined

Took 1m36.341s

(venv) C:\PycharmProjects\Swiggy>