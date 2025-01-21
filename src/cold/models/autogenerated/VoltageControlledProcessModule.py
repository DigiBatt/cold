
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalMeasurementProcessModule import ElectrochemicalMeasurementProcess







class VoltageControlledProcess(ElectrochemicalMeasurementProcess):
    """
    Class representing the `VoltageControlledProcess` entity, which inherits from:
    - ElectrochemicalMeasurementProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46957d35_0f8b_4d92_acb3_aded6ce774a1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VoltageControlledProcess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VoltageControlledProcess(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46957d35_0f8b_4d92_acb3_aded6ce774a1',
    
    class_name='VoltageControlledProcess',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_46957d35_0f8b_4d92_acb3_aded6ce774a1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VoltageControlledProcess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    