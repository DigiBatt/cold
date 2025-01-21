
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalSymbolicConstructModule import ChemicalSymbolicConstruct



from .MathematicalConstructModule import MathematicalConstruct



from .MathematicalModule import Mathematical







class StoichiometricEquation(ChemicalSymbolicConstruct, MathematicalConstruct, Mathematical):
    """
    Class representing the `StoichiometricEquation` entity, which inherits from:
    - ChemicalSymbolicConstruct, MathematicalConstruct, Mathematical

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e72986e_e19f_4c24_8663_cadd4318bd72'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'StoichiometricEquation'`
        - **Alias**: `class_name`
    
    - `iupacReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `iupacReference`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `dbpediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `dbpediaReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = StoichiometricEquation(
    
    class_iri='https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e72986e_e19f_4c24_8663_cadd4318bd72',
    
    class_name='StoichiometricEquation',
    
    iupacReference="example_value",
    
    wikidataReference="example_value",
    
    dbpediaReference="example_value",
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/electrochemistry#electrochemistry_1e72986e_e19f_4c24_8663_cadd4318bd72',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'StoichiometricEquation',
        alias="class_name"
    )
    
    iupacReference: Optional[str] = Field(
        None,
        alias="iupacReference"
    )
    
    wikidataReference: Optional[str] = Field(
        None,
        alias="wikidataReference"
    )
    
    dbpediaReference: Optional[str] = Field(
        None,
        alias="dbpediaReference"
    )
    
    elucidation: Optional[str] = Field(
        None,
        alias="elucidation"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    