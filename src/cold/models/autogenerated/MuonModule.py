
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .SecondGenerationFermionModule import SecondGenerationFermion



from .ElectronTypeModule import ElectronType







class Muon(SecondGenerationFermion, ElectronType):
    """
    Class representing the `Muon` entity, which inherits from:
    - SecondGenerationFermion, ElectronType

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo#EMMO_2531fe94_1cdf_4f36_9abc_7ab7574310db'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Muon'`
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
    obj = Muon(
    
    class_iri='https://w3id.org/emmo#EMMO_2531fe94_1cdf_4f36_9abc_7ab7574310db',
    
    class_name='Muon',
    
    elucidation="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo#EMMO_2531fe94_1cdf_4f36_9abc_7ab7574310db',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Muon',
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
    

    
    

    

    