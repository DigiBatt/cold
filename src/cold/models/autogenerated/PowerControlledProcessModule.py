
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalMeasurementProcessModule import ElectrochemicalMeasurementProcess







class PowerControlledProcess(ElectrochemicalMeasurementProcess):
    """
    Class representing the `PowerControlledProcess` entity, which inherits from:
    - ElectrochemicalMeasurementProcess

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc1af38d_438e_40c2_8a68_0d631a8f46f2'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'PowerControlledProcess'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = PowerControlledProcess(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc1af38d_438e_40c2_8a68_0d631a8f46f2',
    
    class_name='PowerControlledProcess',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_dc1af38d_438e_40c2_8a68_0d631a8f46f2',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'PowerControlledProcess',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    