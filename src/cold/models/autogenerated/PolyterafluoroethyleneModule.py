
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .PolymerCompoundModule import PolymerCompound







class Polyterafluoroethylene(PolymerCompound):
    """
    Class representing the `Polyterafluoroethylene` entity, which inherits from:
    - PolymerCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_e04eb6c9_7de2_46d4_bab2_25ff819d74ab'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Polyterafluoroethylene'`
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
    obj = Polyterafluoroethylene(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_e04eb6c9_7de2_46d4_bab2_25ff819d74ab',
    
    class_name='Polyterafluoroethylene',
    
    pubChemReference="example_value",
    
    wikidataReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_e04eb6c9_7de2_46d4_bab2_25ff819d74ab',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Polyterafluoroethylene',
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
    

    
    

    

    