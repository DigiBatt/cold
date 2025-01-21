
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataSetModule import DataSet







class DischargingData(DataSet):
    """
    Class representing the `DischargingData` entity, which inherits from:
    - DataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a17b9fd0_b005_41eb_b685_e212fc4cecea'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DischargingData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DischargingData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a17b9fd0_b005_41eb_b685_e212fc4cecea',
    
    class_name='DischargingData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_a17b9fd0_b005_41eb_b685_e212fc4cecea',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DischargingData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    