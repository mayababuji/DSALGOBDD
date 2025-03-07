Feature:Login to DS-ALGO Application and validate login page with different scenarios

  @login
  Scenario: To Verify that user is able to land on Login Page
    Given The user is on the DS Algo Home Page
    When The user should click the Sign in link
    Then The user should be redirected to Sign in page and the title of the page should be "Login"

  @login
  Scenario: To Verify that user is able to land on Sign in to DSALGO Page
    Given The user is on the DS Algo Home Page
    When The user should click the Sign in link
    Then The user should be able to able to login with valid credentials and verify the results