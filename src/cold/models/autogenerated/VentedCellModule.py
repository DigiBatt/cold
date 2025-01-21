
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalDeviceModule import ElectrochemicalDevice







class VentedCell(ElectrochemicalDevice):
    """
    Class representing the `VentedCell` entity, which inherits from:
    - ElectrochemicalDevice

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ec1dce8b_bb46_41a9_b532_6bed381aa557'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'VentedCell'`
        - **Alias**: `class_name`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = VentedCell(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ec1dce8b_bb46_41a9_b532_6bed381aa557',
    
    class_name='VentedCell',
    
    IEVReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ec1dce8b_bb46_41a9_b532_6bed381aa557',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'VentedCell',
        alias="class_name"
    )
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    