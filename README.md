# IoTmotes-sensorsDataGen
Information generator of IoT motes sensors to be entered into a database(MySQL + Python3.6)

# Table creation: CaptureValue 



| CaptureValue |
|---|
| ID  |
| Value  |
| sensorID  |
| date  |
| paramID  |

                                                                                                                
# To import it(SQL command): 

    LOAD DATA LOCAL INFILE '/defaultpath/data-CaptureValue.txt' INTO TABLE  CaptureValue COLUMNS TERMINATED BY ',' OPTIONALLY ENCLOSED BY '"'
