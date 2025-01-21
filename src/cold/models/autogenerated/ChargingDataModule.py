
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .DataSetModule import DataSet







class ChargingData(DataSet):
    """
    Class representing the `ChargingData` entity, which inherits from:
    - DataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bf7bfbcb_0698_47af_8678_af92b2f10414'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ChargingData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ChargingData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bf7bfbcb_0698_47af_8678_af92b2f10414',
    
    class_name='ChargingData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_bf7bfbcb_0698_47af_8678_af92b2f10414',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ChargingData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    