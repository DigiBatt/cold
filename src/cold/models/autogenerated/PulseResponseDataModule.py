
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .TimeSeriesElectricalDataSetModule import TimeSeriesElectricalDataSet







class PulseResponseData(TimeSeriesElectricalDataSet):
    """
    Class representing the `PulseResponseData` entity, which inherits from:
    - TimeSeriesElectricalDataSet

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b7f05e67_d7e8_469f_971f_0cb4d4c7e857'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PulseResponseData'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PulseResponseData(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b7f05e67_d7e8_469f_971f_0cb4d4c7e857',
    
    class_name='PulseResponseData',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_b7f05e67_d7e8_469f_971f_0cb4d4c7e857',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PulseResponseData',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    