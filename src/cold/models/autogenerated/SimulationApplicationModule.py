
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ApplicationProgramModule import ApplicationProgram



from .InformationModule import Information



from .FunctionalIconModule import FunctionalIcon







class SimulationApplication(ApplicationProgram, Information, FunctionalIcon):
    """
    Class representing the `SimulationApplication` entity, which inherits from:
    - ApplicationProgram, Information, FunctionalIcon

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_8b66ada5_510c_44bd_a8d8_3c64d301a5e9'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'SimulationApplication'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = SimulationApplication(
    
    class_iri='https://w3id.org/emmo#EMMO_8b66ada5_510c_44bd_a8d8_3c64d301a5e9',
    
    class_name='SimulationApplication',
    
    elucidation="example_value",
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_8b66ada5_510c_44bd_a8d8_3c64d301a5e9',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'SimulationApplication',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    