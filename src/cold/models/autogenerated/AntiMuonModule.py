
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondGenerationFermionModule import SecondGenerationFermion



from .AntiElectronTypeModule import AntiElectronType







class AntiMuon(SecondGenerationFermion, AntiElectronType):
    """
    Class representing the `AntiMuon` entity, which inherits from:
    - SecondGenerationFermion, AntiElectronType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_29ce946a_f164_43ea_b9f8_0cb4f1022853'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'AntiMuon'`
        - **Alias**: `class_name`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = AntiMuon(
    
    class_iri='https://w3id.org/emmo#EMMO_29ce946a_f164_43ea_b9f8_0cb4f1022853',
    
    class_name='AntiMuon',
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_29ce946a_f164_43ea_b9f8_0cb4f1022853',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'AntiMuon',
        alias="class_name"
    )
    

    
    

    

    