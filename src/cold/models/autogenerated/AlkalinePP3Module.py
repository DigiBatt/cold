
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .AlkalineZincManganeseDioxideBatteryModule import AlkalineZincManganeseDioxideBattery







class AlkalinePP3(AlkalineZincManganeseDioxideBattery):
    """
    Class representing the `AlkalinePP3` entity, which inherits from:
    - AlkalineZincManganeseDioxideBattery

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/battery#battery_6e8efa8d_ec92_40e7_8013_e5efb4bc654d'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AlkalinePP3'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AlkalinePP3(
    
    class_iri='https://w3id.org/emmo/domain/battery#battery_6e8efa8d_ec92_40e7_8013_e5efb4bc654d',
    
    class_name='AlkalinePP3',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/battery#battery_6e8efa8d_ec92_40e7_8013_e5efb4bc654d',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AlkalinePP3',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    