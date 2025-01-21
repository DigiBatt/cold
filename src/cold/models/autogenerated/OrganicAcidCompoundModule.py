
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .OrganicCompoundModule import OrganicCompound







class OrganicAcidCompound(OrganicCompound):
    """
    Class representing the `OrganicAcidCompound` entity, which inherits from:
    - OrganicCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_b325bdd7_0adf_4522_a4ef_20cd6929e094'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'OrganicAcidCompound'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = OrganicAcidCompound(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_b325bdd7_0adf_4522_a4ef_20cd6929e094',
    
    class_name='OrganicAcidCompound',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_b325bdd7_0adf_4522_a4ef_20cd6929e094',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'OrganicAcidCompound',
        alias="class_name"
    )
    

    
    

    

    