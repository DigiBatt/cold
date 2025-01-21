
from pydantic import BaseModel, Field, validator
from typing import Optional, List, Union



from .ChemicalCompoundModule import ChemicalCompound







class Solvent(ChemicalCompound):
    """
    Class representing the `Solvent` entity, which inherits from:
    - ChemicalCompound

    This class defines the following attributes:
    
    
    - `class_iri` (`Optional[str]`): 
        - **Default Value**: `'https://w3id.org/emmo/domain/chemical-substance#substance_0f2f65a7_5cc4_4c86_a4d0_676771c646f1'`
        - **Alias**: `class_iri`
    
    - `class_name` (`Optional[str]`): 
        - **Default Value**: `'Solvent'`
        - **Alias**: `class_name`
    
    - `wikidataReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikidataReference`
    
    - `elucidation` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `elucidation`
    
    - `IEVReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `IEVReference`
    
    - `wikipediaReference` (`Optional[str]`): 
        - **Default Value**: `None`
        - **Alias**: `wikipediaReference`
    
    

    Validators are used to ensure that the attributes meet the necessary criteria. These validations are implemented as class methods using Pydantic's `@validator` decorator.
    
    Example usage:
    ```python
    obj = Solvent(
    
    class_iri='https://w3id.org/emmo/domain/chemical-substance#substance_0f2f65a7_5cc4_4c86_a4d0_676771c646f1',
    
    class_name='Solvent',
    
    wikidataReference="example_value",
    
    elucidation="example_value",
    
    IEVReference="example_value",
    
    wikipediaReference="example_value",
    
    ```

    Methods:
    - The class may include custom validation and transformation methods as needed.
    """
    
    
    class_iri: Optional[str] = Field(
        'https://w3id.org/emmo/domain/chemical-substance#substance_0f2f65a7_5cc4_4c86_a4d0_676771c646f1',
        alias="class_iri"
    )
    
    class_name: Optional[str] = Field(
        'Solvent',
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
    
    IEVReference: Optional[str] = Field(
        None,
        alias="IEVReference"
    )
    
    wikipediaReference: Optional[str] = Field(
        None,
        alias="wikipediaReference"
    )
    

    
    

    

    