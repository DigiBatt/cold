
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .FundamentalMatterParticleModule import FundamentalMatterParticle







class Quark(FundamentalMatterParticle):
    """
    Class representing the `Quark` entity, which inherits from:
    - FundamentalMatterParticle

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Quark'`
        - **Alias**: `class_name`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Quark(
    
    class_iri='https://w3id.org/emmo#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105',
    
    class_name='Quark',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_72d53756_7fb1_46ed_980f_83f47efbe105',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Quark',
        alias="class_name"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    