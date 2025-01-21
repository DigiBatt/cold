
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SimulationApplicationModule import SimulationApplication







class EmpiricalSimulationSoftware(SimulationApplication):
    """
    Class representing the `EmpiricalSimulationSoftware` entity, which inherits from:
    - SimulationApplication

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_67c70dcd_2adf_4e6c_b3f8_f33dd1512487'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'EmpiricalSimulationSoftware'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = EmpiricalSimulationSoftware(
    
    class_iri='https://w3id.org/emmo#EMMO_67c70dcd_2adf_4e6c_b3f8_f33dd1512487',
    
    class_name='EmpiricalSimulationSoftware',
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_67c70dcd_2adf_4e6c_b3f8_f33dd1512487',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'EmpiricalSimulationSoftware',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    