
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ReciprocalLengthModule import ReciprocalLength







class Wavenumber(ReciprocalLength):
    """
    Class representing the `Wavenumber` entity, which inherits from:
    - ReciprocalLength

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_d859588d_44dc_4614_bc75_5fcd0058acc8'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Wavenumber'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `qudtReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `qudtReference`
    
    - `ISO80000Reference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `ISO80000Reference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Wavenumber(
    
    class_iri='https://w3id.org/emmo#EMMO_d859588d_44dc_4614_bc75_5fcd0058acc8',
    
    class_name='Wavenumber',
    
    iupacReference="example_value",
    
    qudtReference="example_value",
    
    ISO80000Reference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_d859588d_44dc_4614_bc75_5fcd0058acc8',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Wavenumber',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    qudtReference: Optional[str] = Field(
        None,
        alias="qudtReference"
    )
    
    ISO80000Reference: Optional[str] = Field(
        None,
        alias="ISO80000Reference"
    )
    

    
    

    

    