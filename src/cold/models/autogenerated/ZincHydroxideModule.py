
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .WeakBaseCompoundModule import WeakBaseCompound







class ZincHydroxide(WeakBaseCompound):
    """
    Class representing the `ZincHydroxide` entity, which inherits from:
    - WeakBaseCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_177b95f8_2816_43de_94bb_1a1054c45e32'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ZincHydroxide'`
        - **Alias**: `class_name`
    
    - `pubChemReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `pubChemReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ZincHydroxide(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_177b95f8_2816_43de_94bb_1a1054c45e32',
    
    class_name='ZincHydroxide',
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_177b95f8_2816_43de_94bb_1a1054c45e32',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ZincHydroxide',
        alias="class_name"
    )
    
    pubChemReference: Optional[str] = Field(
        None,
        alias="pubChemReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    