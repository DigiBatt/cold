
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .CoulometryModule import Coulometry







class DirectCoulometryAtControlledPotential(Coulometry):
    """
    Class representing the `DirectCoulometryAtControlledPotential` entity, which inherits from:
    - Coulometry

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DirectCoulometryAtControlledPotential'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'DirectCoulometryAtControlledPotential'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = DirectCoulometryAtControlledPotential(
    
    class_iri='https://w3id.org/emmo/domain/characterisation-methodology/chameo#DirectCoulometryAtControlledPotential',
    
    class_name='DirectCoulometryAtControlledPotential',
    
    iupacReference="example_value",
    
    elucidation="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/characterisation-methodology/chameo#DirectCoulometryAtControlledPotential',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'DirectCoulometryAtControlledPotential',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    

    
    

    

    