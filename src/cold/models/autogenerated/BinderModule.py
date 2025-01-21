
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ElectrochemicalConstituentModule import ElectrochemicalConstituent







class Binder(ElectrochemicalConstituent):
    """
    Class representing the `Binder` entity, which inherits from:
    - ElectrochemicalConstituent

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68eb5e35_5bd8_47b1_9b7f_f67224fa291e'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Binder'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `example` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `example`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Binder(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68eb5e35_5bd8_47b1_9b7f_f67224fa291e',
    
    class_name='Binder',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    example="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_68eb5e35_5bd8_47b1_9b7f_f67224fa291e',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Binder',
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
    
    example: Optional[str] = Field(
        None,
        alias="example"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    