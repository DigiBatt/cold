
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SupercapacitorModule import Supercapacitor







class ElectrochemicalPseudocapacitor(Supercapacitor):
    """
    Class representing the `ElectrochemicalPseudocapacitor` entity, which inherits from:
    - Supercapacitor

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ca0527c1_f682_4eea_aca5_f3ae66a9ddce'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'ElectrochemicalPseudocapacitor'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `comment` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `comment`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = ElectrochemicalPseudocapacitor(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ca0527c1_f682_4eea_aca5_f3ae66a9ddce',
    
    class_name='ElectrochemicalPseudocapacitor',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    comment="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_ca0527c1_f682_4eea_aca5_f3ae66a9ddce',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'ElectrochemicalPseudocapacitor',
        alias="class_name"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    comment: Optional[str] = Field(
        None,
        alias="comment"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    