
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FermionModule import Fermion



from .CompositePhysicalParticleModule import CompositePhysicalParticle







class CompositeFermion(Fermion, CompositePhysicalParticle):
    """
    Class representing the `CompositeFermion` entity, which inherits from:
    - Fermion, CompositePhysicalParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_29108c7c_9087_4992_ab1c_02561665df21'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'CompositeFermion'`
        - **Alias**: `class_name`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = CompositeFermion(
    
    class_iri='https://w3id.org/emmo#EMMO_29108c7c_9087_4992_ab1c_02561665df21',
    
    class_name='CompositeFermion',
    
    example="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_29108c7c_9087_4992_ab1c_02561665df21',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'CompositeFermion',
        alias="class_name"
    )
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    

    
    

    

    